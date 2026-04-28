(function () {
  const state = {
    auto: false,
    speaking: false,
    voices: []
  };

  const controls = document.querySelector(".narration-controls");
  const status = controls ? controls.querySelector("[data-narration-status]") : null;
  const voiceSelect = controls ? controls.querySelector("[data-narration-voice]") : null;
  const rateInput = controls ? controls.querySelector("[data-narration-rate]") : null;
  const rateValue = controls ? controls.querySelector("[data-narration-rate-value]") : null;
  const pauseButton = controls ? controls.querySelector("[data-narration-pause]") : null;
  const captions = document.querySelector(".narration-captions");
  const captionText = captions ? captions.querySelector("[data-narration-caption]") : null;

  function setStatus(text) {
    if (status) status.textContent = text;
  }

  function setPauseLabel(text) {
    if (pauseButton) pauseButton.textContent = text;
  }

  function showCaptions(text) {
    if (!captions || !captionText) return;
    captionText.textContent = text;
    captions.hidden = false;
  }

  function hideCaptions() {
    if (!captions || !captionText) return;
    captionText.textContent = "";
    captions.hidden = true;
  }

  function normalizeNotes(text) {
    return text
      .replace(/Related paper sections?:[^\n]+/gi, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function getCurrentNotes() {
    const slide = Reveal.getCurrentSlide();
    const notes = slide ? slide.querySelector("aside.notes") : null;
    if (!notes) return "";
    return normalizeNotes(notes.textContent || "");
  }

  function selectedVoice() {
    if (!voiceSelect || !voiceSelect.value) return null;
    return state.voices.find((voice) => voice.name === voiceSelect.value) || null;
  }

  function rate() {
    return rateInput ? Number(rateInput.value) : 0.95;
  }

  function updateRateLabel() {
    if (rateValue) rateValue.textContent = `${rate().toFixed(2).replace(/0$/, "")}x`;
  }

  function adjustRate(delta) {
    if (!rateInput) return;
    const min = Number(rateInput.min);
    const max = Number(rateInput.max);
    const next = Math.min(max, Math.max(min, rate() + delta));
    rateInput.value = next.toFixed(2);
    updateRateLabel();
  }

  function populateVoices() {
    if (!("speechSynthesis" in window) || !voiceSelect) return;
    state.voices = window.speechSynthesis.getVoices();
    const englishVoices = state.voices.filter((voice) => /^en(-|_)?/i.test(voice.lang));
    const voices = englishVoices.length ? englishVoices : state.voices;
    voiceSelect.innerHTML = "";
    voices.forEach((voice) => {
      const option = document.createElement("option");
      option.value = voice.name;
      option.textContent = `${voice.name} (${voice.lang})`;
      voiceSelect.appendChild(option);
    });
  }

  function stopNarration() {
    state.auto = false;
    state.speaking = false;
    state.paused = false;
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    setPauseLabel("Pause");
    hideCaptions();
    setStatus("Stopped");
  }

  function togglePause() {
    if (!("speechSynthesis" in window) || !state.speaking) return;
    if (state.paused) {
      window.speechSynthesis.resume();
      state.paused = false;
      setPauseLabel("Pause");
      setStatus(state.auto ? "Auto narrating" : "Narrating slide");
    } else {
      window.speechSynthesis.pause();
      state.paused = true;
      setPauseLabel("Resume");
      setStatus("Paused");
    }
  }

  function speakCurrent(autoAdvance) {
    if (!("speechSynthesis" in window)) {
      setStatus("Speech not supported in this browser");
      return;
    }

    const text = getCurrentNotes();
    if (!text) {
      setStatus("No notes on this slide");
      return;
    }

    window.speechSynthesis.cancel();
    state.paused = false;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = rate();
    utterance.pitch = 1;
    const voice = selectedVoice();
    if (voice) utterance.voice = voice;

    state.speaking = true;
    state.auto = Boolean(autoAdvance);
    setPauseLabel("Pause");
    showCaptions(text);
    setStatus(state.auto ? "Auto narrating" : "Narrating slide");

    utterance.onend = function () {
      state.speaking = false;
      state.paused = false;
      setPauseLabel("Pause");
      if (state.auto) {
        const index = Reveal.getIndices();
        const total = Reveal.getTotalSlides();
        if (index.h + 1 < total) {
          Reveal.next();
          window.setTimeout(() => speakCurrent(true), 500);
        } else {
          state.auto = false;
          setStatus("Finished");
        }
      } else {
        hideCaptions();
        setStatus("Ready");
      }
    };

    utterance.onerror = function () {
      state.speaking = false;
      state.auto = false;
      state.paused = false;
      setPauseLabel("Pause");
      hideCaptions();
      setStatus("Narration error");
    };

    window.speechSynthesis.speak(utterance);
  }

  function bindControls() {
    if (!controls) return;
    controls.querySelector("[data-narration-current]")?.addEventListener("click", () => speakCurrent(false));
    controls.querySelector("[data-narration-auto]")?.addEventListener("click", () => speakCurrent(true));
    controls.querySelector("[data-narration-pause]")?.addEventListener("click", togglePause);
    controls.querySelector("[data-narration-stop]")?.addEventListener("click", stopNarration);
    controls.querySelector("[data-narration-slower]")?.addEventListener("click", () => adjustRate(-0.1));
    controls.querySelector("[data-narration-faster]")?.addEventListener("click", () => adjustRate(0.1));
    rateInput?.addEventListener("input", updateRateLabel);
  }

  function bindKeys() {
    window.addEventListener("keydown", (event) => {
      if (event.target && ["INPUT", "SELECT", "TEXTAREA"].includes(event.target.tagName)) return;
      if (event.key === "n" || event.key === "N") {
        event.preventDefault();
        speakCurrent(false);
      }
      if (event.key === "a" || event.key === "A") {
        event.preventDefault();
        speakCurrent(true);
      }
      if (event.key === "x" || event.key === "X") {
        event.preventDefault();
        stopNarration();
      }
      if (event.key === "p" || event.key === "P") {
        event.preventDefault();
        togglePause();
      }
    });
  }

  function init() {
    bindControls();
    bindKeys();
    populateVoices();
    updateRateLabel();
    if ("speechSynthesis" in window) {
      window.speechSynthesis.onvoiceschanged = populateVoices;
      setStatus("Ready");
    } else {
      setStatus("Speech not supported");
    }
  }

  if (window.Reveal) {
    Reveal.on("ready", init);
    if (Reveal.isReady && Reveal.isReady()) init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
