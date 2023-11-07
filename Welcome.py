from st_pages import Page, Section, show_pages, add_page_title

add_page_title("hello") # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Welcome.py", "Home", "🏠"),
        Section("Additional Projects", icon="🎈️"),
        Page("pages/analyducks.py", "Analyducks"),
        # Page("pages/pokedex.py", "Pokedex"),
        # # Pages after a section will be indented
        # Page("Another page", icon="💪"),
        # # Unless you explicitly say in_section=False
        # Page("Not in a section", in_section=False)
    ]
  )

