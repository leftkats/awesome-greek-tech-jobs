import yaml
from jinja2 import Template
import datetime

# 1. Load the companies data
try:
    with open("data/companies.yaml", "r", encoding="utf-8") as f:
        # Resolves &anchors and *aliases
        companies_data = yaml.load(f, Loader=yaml.FullLoader)
except FileNotFoundError:
    print("Error: companies.yaml not found!")
    exit()

# 2. Define the Template
template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Awesome Greek Tech Jobs | Production</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { "primary": "#000000", "background": "#ffffff" },
                    fontFamily: { "display": ["Inter", "sans-serif"], "mono": ["JetBrains Mono", "monospace"] }
                },
            },
        }
    </script>
    <style type="text/tailwindcss">
        @layer base {
            body { @apply bg-background text-black font-display antialiased; }
            .brutalist-border { @apply border border-black; }
            .mono-text { @apply font-mono uppercase tracking-tight; }
            .no-scrollbar::-webkit-scrollbar { display: none; }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">
    <div class="bg-black text-white px-4 py-3 brutalist-border border-x-0 border-t-0 flex items-start gap-3">
        <span class="material-symbols-outlined text-sm mt-0.5">warning</span>
        <div class="text-[11px] leading-tight uppercase font-bold tracking-tight">
            NOTICE: This is a statically generated site. Data accuracy is dependent on source repository updates. 
            <span class="text-yellow-400 underline underline-offset-2">Remote/Location policies are currently under construction</span> and may not reflect real-time changes.
        </div>
    </div>

    <nav class="sticky top-0 z-50 bg-background brutalist-border border-x-0 border-t-0 px-4 py-4 flex items-center justify-between">
        <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-xl">database</span>
            <span class="font-bold text-xs mono-text">AGTJ // SOURCE.YAML</span>
        </div>
        <a href="https://github.com/leftkats/awesome-greek-tech-jobs"><span class="material-symbols-outlined">terminal</span></a>
    </nav>

    <header class="px-4 pt-8 pb-6 border-b brutalist-border border-x-0 border-t-0">
        <h1 class="text-4xl font-extrabold tracking-tighter uppercase mb-4">Awesome Greek<br />Tech Jobs</h1>
        <p class="text-xs font-bold mono-text max-w-xs">[A curated list of Greek tech companies and their career portals]</p>
    </header>

    <section class="p-4">
        <div class="flex brutalist-border bg-white overflow-hidden">
            <div class="flex items-center justify-center px-3 border-r brutalist-border"><span class="material-symbols-outlined">search</span></div>
            <input id="searchInput" class="w-full p-3 text-xs mono-text border-none focus:ring-0 bg-transparent" placeholder="Filter by company or sector..." type="text" onkeyup="filterData()" />
        </div>
    </section>

    <main class="flex-grow" id="companyList">
        {% for company in companies %}
        <div class="company-card flex p-4 brutalist-border border-t-0 border-x-0 hover:bg-gray-50 transition-colors" 
             data-name="{{ company.name }}" 
             data-sectors="{{ company.sectors|join(' ') }}">
            <div class="flex-1 space-y-2">
                <div class="flex items-center gap-2">
                    <h2 class="text-xl font-extrabold uppercase leading-none">{{ company.name }}</h2>
                    <span class="text-[9px] brutalist-border px-1.5 py-0.5 font-bold mono-text bg-white">GREECE</span>
                </div>
                <div class="flex flex-wrap gap-1">
                    {% for sector in company.sectors %}
                    <span class="text-[9px] mono-text border border-black/20 px-1 py-0.5">{{ sector }}</span>
                    {% endfor %}
                </div>
            </div>
            <div class="flex items-center justify-end pl-4">
                <a class="brutalist-border p-3 flex items-center justify-center hover:bg-black hover:text-white transition-all active:scale-95" href="{{ company.careers_url }}" target="_blank">
                    <span class="material-symbols-outlined text-lg">open_in_new</span>
                </a>
            </div>
        </div>
        {% endfor %}
    </main>

    <footer class="p-8 flex flex-col items-center justify-center border-t brutalist-border border-x-0">
        <p class="text-[9px] font-bold mono-text opacity-40 uppercase">Last Build: {{ build_time }}</p>
    </footer>

    <script>
        function filterData() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.getElementsByClassName('company-card');
            for (let card of cards) {
                const searchStr = (card.dataset.name + ' ' + card.dataset.sectors).toLowerCase();
                card.style.display = searchStr.includes(query) ? 'flex' : 'none';
            }
        }
    </script>
</body>
</html>
"""

# 3. Render and Save
build_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
template = Template(template_str)
final_html = template.render(companies=companies_data, build_time=build_now)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"index.html generated at {build_now}")
