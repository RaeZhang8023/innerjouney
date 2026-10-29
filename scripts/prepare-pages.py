from pathlib import Path
import re,shutil
source=Path(__file__).resolve().parents[2]/'phone-preview/dist'
root=Path(__file__).resolve().parents[1]/'docs'
base='/innerjouney/'
root.mkdir(exist_ok=True)
shutil.copytree(source,root,dirs_exist_ok=True)
# Native bundle assets and dependency paths are unused by this browser build.
shutil.rmtree(root/'assets/node_modules',ignore_errors=True)
shutil.rmtree(root/'.openai',ignore_errors=True)
for p in list(root.rglob('*')):
 if p.is_file() and (p.name.startswith('._') or p.name=='.DS_Store'):p.unlink()
 if p.is_file() and p.suffix in ['.js','.html','.css']:
  text=p.read_text()
  for quote in ['"',"'",'`']:
   for directory in ['assets','_expo']:
    text=text.replace(quote+'/'+directory+'/',quote+base+directory+'/')
  p.write_text(text)
(root/'.nojekyll').touch()
urls=set()
for p in root.rglob('*.js'):
 urls.update(re.findall(r'[\"\']('+re.escape(base)+r'assets/[^\"\']+)[\"\']',p.read_text()))
for url in urls:
 if not (root/url[len(base):]).is_file():raise SystemExit('Missing referenced asset: '+url)
# Remove native-only duplicates from a combined Expo export.
used={u[len(base):] for u in urls}
for p in (root/'assets').rglob('*'):
 if p.is_file() and p.relative_to(root).as_posix() not in used:p.unlink()
print(f'Prepared {len(urls)} web assets for {base}')
