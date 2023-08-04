require.config({ paths: { 'vs': 'https://cdn.jsdelivr.net/npm/monaco-editor@0.27.0/min/vs' } });

require(['vs/editor/editor.main'], function() {
    // Set the theme to 'vs-dark'
    monaco.editor.setTheme('vs-dark');

    var editor = monaco.editor.create(document.getElementById('container'), {
        value: "//Write Code Here",
        language: "javascript"
    });

    var submitButton = document.getElementById('convertCode');
    submitButton.addEventListener('click', function() {
        var code = editor.getValue();
        console.log('Submitted code:', code);
        // You can perform further actions with the submitted code here
    });
});
