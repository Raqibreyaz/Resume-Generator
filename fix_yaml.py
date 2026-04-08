import yaml

with open('info/basic-info.yaml') as f:
    basic_info = yaml.safe_load(f)

with open('Test_User_CV.yaml') as f:
    test_cv = yaml.safe_load(f)

# Keep the CV block (the content)
new_basic_info = {
    "cv": basic_info["cv"],
    "design": test_cv["design"],
    "locale": test_cv["locale"],
    "settings": test_cv["settings"]
}

# Apply our design customizations
new_basic_info["design"]["typography"] = {
    "font_family": {
        "body": "Source Sans 3",
        "name": "Source Sans 3",
        "headline": "Source Sans 3",
        "connections": "Source Sans 3",
        "section_titles": "Source Sans 3"
    },
    "font_size": {
        "body": "10pt",
        "name": "24pt",
        "headline": "10pt",
        "connections": "10pt",
        "section_titles": "1.2em"
    },
    "line_spacing": "0.25em",
    "alignment": "justified",
    "date_and_location_column_alignment": "right",
    "small_caps": {"name": False, "headline": False, "connections": False, "section_titles": False},
    "bold": {"name": True, "headline": False, "connections": False, "section_titles": True}
}

new_basic_info["design"]["header"] = {
    "alignment": "center",
    "photo_width": "3.5cm",
    "photo_position": "left",
    "photo_space_left": "0.4cm",
    "photo_space_right": "0.4cm",
    "space_below_name": "0.3cm",
    "space_below_headline": "0.3cm",
    "space_below_connections": "0.3cm",
    "connections": {
        "hyperlink": True,
        "show_icons": False,
        "display_urls_instead_of_usernames": True,
        "separator": "|",
        "space_between_connections": "0.15cm"
    }
}

title_type = new_basic_info["design"]["section_titles"].get("type", "with_full_line")
new_basic_info["design"]["section_titles"] = {
    "type": "with_full_line",
    "line_thickness": "0.8pt",
    "space_above": "0.55cm",
    "space_below": "0.2cm"
}

new_basic_info["design"]["sections"] = {
    "allow_page_break": True,
    "space_between_regular_entries": "0.4cm",
    "space_between_text_based_entries": "0.2cm"
}

# Update Templates from basic-info
new_basic_info["design"]["templates"] = test_cv["design"]["templates"]

new_basic_info["design"]["templates"]["education_entry"] = {
    "main_column": "**INSTITUTION**\n\n*DEGREE* in *AREA*",
    "date_and_location_column": "*LOCATION*\n\n*DATE*",
    "degree_column": ""
}

new_basic_info["design"]["templates"]["experience_entry"] = {
    "main_column": "**POSITION**, COMPANY -- LOCATION\nSUMMARY\nHIGHLIGHTS",
    "date_and_location_column": "DATE"
}

new_basic_info["design"]["templates"]["normal_entry"] = {
    "main_column": "NAME -- **LOCATION**\nSUMMARY\nHIGHLIGHTS",
    "date_and_location_column": "DATE"
}

new_basic_info["design"]["templates"]["publication_entry"] = {
    "main_column": "**TITLE**\nAUTHORS\nURL (JOURNAL)",
    "date_and_location_column": "DATE"
}

new_basic_info["design"]["templates"]["one_line_entry"] = {
    "main_column": "**LABEL:** DETAILS"
}

with open('info/basic-info.yaml', 'w') as f:
    yaml.dump(new_basic_info, f, sort_keys=False, allow_unicode=True)

