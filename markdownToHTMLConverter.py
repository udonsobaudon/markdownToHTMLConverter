import sys
import markdown

l = len(sys.argv)
md = markdown.Markdown(extensions=['tables', 'md_in_html', 'attr_list'])

if l != 4:
    print('Error!')
    sys.exit()
if sys.argv[1] != 'markdown':
    print('Error!')
    sys.exit()
else :
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]
    try:
        with open(inputfile) as f:
            contents = f.read()
            markdownToHTML = md.convert(contents)
        with open(outputfile, 'w') as f:
            f.write(markdownToHTML)
    except FileNotFoundError:
        print('File not found error')

