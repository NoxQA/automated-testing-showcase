#!/bin/bash

# Base directory for the tests
BASE_DIR="./tests"

# Array of folders and their respective files
declare -A folders_and_files=(
    ["/auth"]="test_basic_auth.py test_digest_auth.py test_form_auth.py"
    ["/elements"]="test_add_remove_elements.py test_checkboxes.py test_dropdown.py test_inputs.py"
    ["/interaction"]="test_drag_and_drop.py test_context_menu.py test_hover.py test_floating_menu.py test_horizontal_slider.py"
    ["/file_management"]="test_file_upload.py test_file_download.py test_secure_file_download.py"
    ["/dynamic_content"]="test_dynamic_content.py test_dynamic_controls.py test_dynamic_loading.py test_disappearing_elements.py"
    ["/frames"]="test_frames.py test_nested_frames.py"
    ["/notifications"]="test_notification_messages.py test_entry_ad.py test_exit_intent.py"
    ["/misc"]="test_ab_testing.py test_broken_images.py test_challenging_dom.py test_redirect_link.py test_large_deep_dom.py test_slow_resources.py test_typos.py test_status_codes.py"
    ["/shadow"]="test_shadow_dom.py"
    ["/tables"]="test_sortable_data_tables.py"
    ["/alerts"]="test_javascript_alerts.py test_javascript_onload_error.py"
    ["/keys"]="test_key_presses.py"
    ["/editors"]="test_wysiwyg_editor.py"
    ["/menu"]="test_jquery_ui_menus.py"
    ["/scroll"]="test_infinite_scroll.py"
    ["/geolocation"]="test_geolocation.py"
)

# Function to create folders and files
create_structure() {
    for folder in "${!folders_and_files[@]}"; do
        # Create directory if it doesn't exist
        mkdir -p "$BASE_DIR$folder"
        
        # Create each file within the folder
        for file in ${folders_and_files[$folder]}; do
            touch "$BASE_DIR$folder/$file"
        done
    done
}

# Update README.md
update_readme() {
    cat <<EOL > README.md
# Selenium Automation Showcase

## Project Structure

This project showcases automated tests for various scenarios using [the-internet](https://the-internet.herokuapp.com/). The tests are organized into different categories based on functionality:

\`\`\`
/tests
    /auth
        - test_basic_auth.py: Tests basic authentication.
        - test_digest_auth.py: Tests digest authentication.
        - test_form_auth.py: Tests form-based authentication.
/elements
        - test_add_remove_elements.py: Tests adding and removing elements.
        - test_checkboxes.py: Tests checkbox interactions.
        - test_dropdown.py: Tests dropdown interactions.
        - test_inputs.py: Tests input field interactions.
/interaction
        - test_drag_and_drop.py: Tests drag and drop functionality.
        - test_context_menu.py: Tests right-click context menu interactions.
        - test_hover.py: Tests hover interactions.
        - test_floating_menu.py: Tests interactions with floating menus.
        - test_horizontal_slider.py: Tests slider functionality.
/file_management
        - test_file_upload.py: Tests file upload functionality.
        - test_file_download.py: Tests file download functionality.
        - test_secure_file_download.py: Tests secure file download functionality.
/dynamic_content
        - test_dynamic_content.py: Tests for dynamic content loading.
        - test_dynamic_controls.py: Tests for dynamic controls.
        - test_dynamic_loading.py: Tests dynamic page loading.
        - test_disappearing_elements.py: Tests elements that disappear dynamically.
/frames
        - test_frames.py: Tests interaction with frames.
        - test_nested_frames.py: Tests nested frames.
/notifications
        - test_notification_messages.py: Tests notification message displays.
        - test_entry_ad.py: Tests entry ads pop-up.
        - test_exit_intent.py: Tests exit intent functionality.
/misc
        - test_ab_testing.py: Tests A/B testing scenarios.
        - test_broken_images.py: Tests broken image detection.
        - test_challenging_dom.py: Tests challenging DOM elements.
        - test_redirect_link.py: Tests page redirection.
        - test_large_deep_dom.py: Tests interaction with large & deep DOM.
        - test_slow_resources.py: Tests slow-loading resources.
        - test_typos.py: Tests for typographical errors.
        - test_status_codes.py: Tests handling of various HTTP status codes.
/shadow
        - test_shadow_dom.py: Tests interactions with Shadow DOM elements.
/tables
        - test_sortable_data_tables.py: Tests sortable data tables.
/alerts
        - test_javascript_alerts.py: Tests JavaScript alerts.
        - test_javascript_onload_error.py: Tests JavaScript onload event errors.
/keys
        - test_key_presses.py: Tests keyboard actions.
/editors
        - test_wysiwyg_editor.py: Tests WYSIWYG editor interactions.
/menu
        - test_jquery_ui_menus.py: Tests JQuery UI menu interactions.
/scroll
        - test_infinite_scroll.py: Tests infinite scrolling.
/geolocation
        - test_geolocation.py: Tests geolocation interactions.
\`\`\`

## Installation

Make sure you have Python and pip installed. Then, install the dependencies with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

To run the tests, execute the following command:

\`\`\`bash
pytest
\`\`\`

## About

This project is a demonstration of my skills as a QA Engineer. It showcases a variety of automated Selenium tests for different web scenarios, organized for clarity and easy navigation.

## License

This project is open-source and available under the MIT License.
EOL
}

# Create the folder and file structure
create_structure

# Update the README
update_readme

# Notify user of completion
echo "Folder structure, test files, and README.md have been set up successfully!"
