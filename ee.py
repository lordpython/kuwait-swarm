import markdown

# Load markdown data

with open('edd.md', 'r') as file:
    md_data = file.read()
    
# Convert markdown to HTML
html_data = markdown.markdown(md_data)

# Save HTML data to a file
with open('edd.html', 'w') as file:
    file.write(html_data)
    