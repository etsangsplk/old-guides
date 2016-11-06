#!/usr/bin/python
import sys
if len(sys.argv) == 1:
    print """Usage:
    * Use Atom editor with 'Markdown Preview Plus' to open one of the _output/_*.md files created by build.sh and press ctrl+shift+m to render it to HTML
    * Right click on the HTML preview and 'Save as HTML...'
    * Run convert.py _output/_file.md.html
This will save the resulting 'tidied up' file as _output/_file.html
Open it in Atom and copy and paste it into Wordpress.
    """
    sys.exit(1)
html = open(sys.argv[1]).read()
start = "<body class='markdown-preview' data-use-github-style>"
end = "</html>"
html = html.split(start)[1]
html = html.split(end)[0]
html = html.replace("/Users/luke/Projects/Weave/guides/weave-cloud-microservices/_output/", "/wp-content/uploads/")
f = open(sys.argv[1].replace(".md.html", ".html"), 'w')
f.write("""
<!--








DO NOT EDIT THIS FILE DIRECTLY

See https://github.com/weaveworks/guides/tree/master/weave-cloud-microservices






-->
""")
f.write(html)
f.close()
