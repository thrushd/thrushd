## Personal Website Source

A personal website built using [pelican](https://blog.getpelican.com/) and the [Flex theme](https://github.com/alexandrevicenzi/Flex/tree/master).

I relied heavily on [this](https://spapas.github.io/2013/10/07/pelican-static-windows/) tutorial, which is fantastic!

I added some custom colors to make it feel more like my own. For that I copied the sections of the Flex theme's style.less file that included colors I wanted to change. Then I wrote a simple python script to compile the LESS to CSS when I generate content with `pelrun.bat`.

### Instructions (for future me)

#### Fresh environment setup
1. `pip install pelican`
2. `pip install lesscpy`
3. `pip install markdown`
4. Create a folder called `pelican` and navigate inside
5. Run `git clone https://github.com/thrushd/thrushd.git` to clone the main repository
6. Run `https://github.com/getpelican/pelican-themes.git` to clone the theme repository
7. Navigate to `thrushd` and run `git switch source` to switch to the source branch for editing

#### New content generation
1. Generate content
2. Run `start pelrun.bat` in powershell
3. Check for warnings and missing files
4. Run `start pelserve.bat`. Navigate to [http://localhost:8000](http://localhost:8000) and check the new content
5. Correct errors as needed
6. Push new content to github with `start ghdeploy.bat`
