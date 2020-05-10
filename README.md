## Personal Website Source

A personal website built using [pelican](https://blog.getpelican.com/) and the [Flex theme](https://github.com/alexandrevicenzi/Flex/tree/master).

I relied heavily on [this](https://spapas.github.io/2013/10/07/pelican-static-windows/) tutorial, which is fantastic!

I added some custom colors to make it feel more like my own. For that I copied the sections of the Flex theme's style.less file that included colors I wanted to change. Then I wrote a simple python script to compile the LESS to CSS when I generate content with `pelrun.bat`.

### Instructions (for future me)

1. Generate content
2. Run `start pelrun.bat` in powershell
3. Check for warnings and missing files
4. Run `start pelserve.bat`. Navigate to [http://localhost:8000](http://localhost:8000) and preview all the new content
5. Correct errors as needed
6. Publish new content with `start pelpub.bat`
7. Push new content to github with `start ghdeploy.bat`
