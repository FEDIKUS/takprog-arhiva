window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    // The configuration can load before the deferred MathJax runtime.
    // Its initial startup handles this page; subsequent navigation uses typesetPromise.
    if (typeof MathJax.typesetPromise === "function") MathJax.typesetPromise()
  })
  