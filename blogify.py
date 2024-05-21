import os
import shutil
from bs4 import BeautifulSoup

# Define the CSS and JS to be added
css_content = """
<style>
h1 {
  color: #3c4858;
  font-size: 24px;
  font-family: Calibri, sans-serif;
  text-align: center;
}
h2 {
  color: #3c4858;
  font-size: 20px;
  font-family: Calibri, sans-serif;
  text-align: center;
}
p {
  color: #8492a6;
  font-size: 16px;
  font-family: Calibri, sans-serif;
}
img {
  max-width: 370px;
  height: auto;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
a {
  text-decoration: none;
  color: inherit;
}
.blog-section {
  background-color: #f0f0f0;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 20px;
  padding: 20px;
  text-align: center;
  max-width: 450px;
  margin-left: auto;
  margin-right: auto;
}
.read-more-button {
  background-color: #36b37e; /* Updated green color */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  font-family: Arial, sans-serif;
  margin-top: 10px;
  border-radius: 25px; /* Pill-shaped button */
  cursor: pointer;
}
.read-more-button:hover {
  background-color: #2a9566;
}
.expert-assistance-button {
  background-color: #36b37e; /* Updated green color */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  font-family: Arial, sans-serif;
  margin-top: 10px;
  border-radius: 25px; /* Pill-shaped button */
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.expert-assistance-button:hover {
  background-color: #2a9566;
}
.centered-paragraph {
  text-align: center;
  color: #3c4858;
  font-size: 18px;
  font-family: Calibri, sans-serif;
  margin-bottom: 10px;
}
</style>
"""

js_content = """
<script>
document.addEventListener("DOMContentLoaded", function() {
  const navbar = document.createElement('div');
  navbar.id = 'sticky-navbar';

  // Styling for the navbar
  navbar.style.cssText = `
    position: sticky;
    top: 0;
    width: 100%;
    padding: 20px 20px; 
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    background-color: #16A9DE; 
    color: white;
    font-family: 'Nunito Sans', Calibri, sans-serif;
  `;

  // Logo 
  const logo = document.createElement('a');
  logo.href = '../../index.html';  // Link to the local blog index
  const logoImg = document.createElement('img');
  logoImg.src = 'https://lendingwyse.com/imagehosting/9376/14198-lendwyselogolongwht-01.png';
  logoImg.alt = 'lendwyse';
  logoImg.style.maxHeight = '60px';
  logo.appendChild(logoImg);

  // Wrapper for the logo to add margin
  const logoWrapper = document.createElement('div');
  logoWrapper.style.marginLeft = '7px';
  logoWrapper.appendChild(logo);
  navbar.appendChild(logoWrapper);

  // Dropdown Container
  const dropdownContainer = document.createElement('div');
  dropdownContainer.style.display = 'flex';
  dropdownContainer.style.flexDirection = 'column';
  dropdownContainer.style.alignItems = 'flex-end';
  dropdownContainer.style.marginLeft = 'auto';
  dropdownContainer.style.marginRight = '30px'; // More space from the right

  // Label
  const label = document.createElement('label');
  label.textContent = 'See Lending Options:';
  label.style.fontSize = '16px';
  label.style.marginBottom = '10px'; 
  dropdownContainer.appendChild(label);

  // Dropdown
  const dropdown = document.createElement('select');
  // Inline CSS for the dropdown
  dropdown.style.cssText = `
    padding: 0.75rem 1.25rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #8492A6;
    background-color: #FFF;
    background-clip: padding-box;
    border: 1px solid #E0E6ED;
    border-radius: 0.25rem;
    box-shadow: inset 0 1px 1px rgba(31, 45, 61, 0.075);
  `;

  // Placeholder option
  const placeholder = document.createElement('option');
  placeholder.text = 'Amount you want to borrow?';
  placeholder.disabled = true;
  placeholder.selected = true;
  dropdown.add(placeholder);

  const options = [
    ["$0-$4,999", 2500], 
    ["$5,000-$7,499", 6250], 
    ["$7,500-$9,999", 8750],
    ["$10,000-$14,999", 12500],
    ["$15,000-$19,999", 17500],
    ["$20,000-$29,999", 25000],
    ["$30,000-$39,999", 35000],
    ["$40,000-$49,999", 45000],
    ["$50,000-$59,999", 55000],
    ["$60,000-$69,999", 65000],
    ["$70,000-$79,999", 75000],
    ["$80,000-$89,999", 85000],
    ["$90,000-$99,999", 95000],
    ["$100,000+", 100000]
  ];
  options.forEach(([text, value]) => {
    const option = document.createElement('option');
    option.text = text;
    option.value = value;
    dropdown.add(option);
  });

  dropdown.addEventListener('change', function() {
    window.location.href = `https://lendwyse.com/apply-now?amount=${this.value}`;
  });
  dropdownContainer.appendChild(dropdown);
  
  navbar.appendChild(dropdownContainer); 

  // Responsive behavior
  function handleResize() {
    if (window.innerWidth < 576) { // Adjust breakpoint to 576px
      navbar.style.flexDirection = 'column';
      logoImg.src = 'https://lendingwyse.com/imagehosting/9376/14199-squarewhtlwlogo-01.png'; // Change logo image
      logoWrapper.style.marginLeft = '0';
      dropdownContainer.style.marginLeft = '0';
      dropdownContainer.style.marginRight = '0';
      dropdownContainer.style.alignItems = 'center';
      dropdownContainer.style.width = '100%';
      label.style.marginBottom = '5px'; 
    } else {
      navbar.style.flexDirection = 'row';
      logoImg.src = 'https://lendingwyse.com/imagehosting/9376/14198-lendwyselogolongwht-01.png'; // Revert logo image
      logoWrapper.style.marginLeft = '7px';
      dropdownContainer.style.marginLeft = 'auto';
      dropdownContainer.style.marginRight = '30px'; // More space from the right
      dropdownContainer.style.alignItems = 'flex-end';
      dropdownContainer.style.width = 'auto';
      label.style.marginBottom = '10px';
    }
  }

  window.addEventListener('resize', handleResize);
  handleResize(); 

  document.body.prepend(navbar); 
});
</script>
"""

# Directory containing the blog folders
base_dir = os.path.dirname(os.path.abspath(__file__))
resources_dir = os.path.join(base_dir, 'resources')

# Create resources directory if it doesn't exist
if not os.path.exists(resources_dir):
    os.makedirs(resources_dir)

# List to hold blog details for the index
blog_details = []

# Function to update HTML files and extract details
def update_html_files():
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path) and folder != 'resources':
            new_folder_path = os.path.join(resources_dir, folder)
            shutil.move(folder_path, new_folder_path)
            folder_path = new_folder_path
            for file in os.listdir(folder_path):
                if file.endswith('.html'):
                    html_path = os.path.join(folder_path, file)
                    with open(html_path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f, 'html.parser')

                    # Add CSS to head
                    head = soup.find('head')
                    if head:
                        head.append(BeautifulSoup(css_content, 'html.parser'))

                    # Add JS before closing body tag
                    body = soup.find('body')
                    if body:
                        script_tag = BeautifulSoup(js_content, 'html.parser')
                        body.append(script_tag)

                    # Remove the first h2 and the preceding image
                    first_h2 = soup.find('h2')
                    if first_h2:
                        prev_sibling = first_h2.find_previous_sibling('img')
                        if prev_sibling:
                            prev_sibling.decompose()
                        first_h2.decompose()

                    # Extract h1 title and the first image
                    h1_title = soup.find('h1').get_text()
                    first_img = soup.find('img')['src']

                    # Save the updated HTML
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

                    # Store the details for index
                    blog_details.append((h1_title, os.path.join('resources', folder, file), os.path.join('resources', folder, first_img)))

# Function to create the index HTML file
def create_index_html():
    index_path = os.path.join(base_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('<html><head>')
        f.write(css_content)
        f.write('</head><body>')
        f.write('<h1>Considering a Personal Loan?</h1>')
        f.write('<h2>With inflation looming, a loan up to $100k at reasonable rates could help you achieve the financial nirvana you are looking for.</h2>')
        f.write('<p class="centered-paragraph">Read through the following resources about personal loans, or click below to schedule expert assistance and find the perfect plan for you.</p>')
        f.write('<a href="https://lendwyse.com/?blog" class="expert-assistance-button">Get Expert Lending Assistance</a>')
        
        f.write('<div style="display: flex; flex-wrap: wrap;">')
        for title, link, img in blog_details:
            f.write(f'<div class="blog-section">')
            f.write(f'<a href="{link}"><h2>{title}</h2></a>')
            f.write(f'<a href="{link}"><img src="{img}" style="width: 100%;"></a>')
            f.write(f'<a href="{link}" class="read-more-button">Read More</a>')
            f.write('</div>')
        f.write('</div>')
        
        f.write(js_content)
        f.write('</body></html>')

# Run the functions
update_html_files()
create_index_html()
