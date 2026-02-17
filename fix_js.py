import os

files = [
    "index.html", "about.html", "services.html", "gallery.html",
    "videos.html", "contact.html", "Festival26.html", "Festival25.html",
    "Festival24.html", "Festival23.html"
]

script_content = """
   <script>
      document.addEventListener('DOMContentLoaded', function () {
         // Festival Dropdown Toggle
         var dropdownToggle = document.getElementById('dropdown-toggle');
         var dropdownMenu = document.getElementById('dropdown-menu');
         if (dropdownToggle && dropdownMenu) {
            dropdownToggle.addEventListener('click', function (e) {
               e.preventDefault();
               dropdownMenu.classList.toggle('active');
            });
         }

         // Mobile Menu Toggler Fallback
         var navbarToggler = document.querySelector('.navbar-toggler');
         var navbarCollapse = document.getElementById('navbarNav');
         if (navbarToggler && navbarCollapse) {
            navbarToggler.addEventListener('click', function () {
               navbarCollapse.classList.toggle('show');
            });
         }
      });
   </script>
"""

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Standardize script by replacing existing versions
    import re
    # Strip any existing dropdown toggle scripts I added before to avoid duplicates
    # Use a broad regex to find my previous script block
    content = re.sub(r' <script>\s*document.addEventListener\(\'DOMContentLoaded\', function \(\) \{.*?\}\);\s*</script>', '', content, flags=re.DOTALL)

    # Insert before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', script_content + '\n</body>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated script in {filename}")
    else:
        print(f"Could not find </body> in {filename}")
