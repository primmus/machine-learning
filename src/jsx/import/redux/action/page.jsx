/**
 * page.jsx: send current support vector 'submit button' boolean, indication
 *           whether it should be displayed to the redux store.
 *
 */

function setSvButton(action) {
    return {
        type: 'SUBMIT-SV-ANALYSIS',
        button: {
            submit_analysis: action.button.submit_analysis
        }
    };
}

function setGotoResultsButton(action) {
    return {
        type: 'GOTO-RESULTS',
        button: {
            goto_results: action.button.goto_results
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export { setSvButton, setGotoResultsButton }
