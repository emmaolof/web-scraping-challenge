{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "from pprint import pprint\n",
    "import time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Scraping \n",
    "\n",
    "##### 1.1. NASA Mars News\n",
    "\n",
    "* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.\n",
    "\n",
    "From URL to beautiful soup object\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "#URL of page to be scrapped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "#start hacking\n",
    "executable_path = {'executable_path':'chromedriver'}\n",
    "browser = Browser('chrome',**executable_path,headless=False)\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The title is: \n",
      "The MarCO Mission Comes to an End\n",
      "\n",
      "The descriptive paragraph is:  \n",
      "The pair of briefcase-sized satellites made history when they sailed past Mars in 2019.\n"
     ]
    }
   ],
   "source": [
    "#collect latest news and print\n",
    "html = browser.html\n",
    "mars_soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "\n",
    " # find the first news title\n",
    "news_title = mars_soup.body.find(\"div\", class_=\"content_title\").text\n",
    "# find the paragraph associated with the first title\n",
    "news_paragraph = mars_soup.body.find(\"div\", class_=\"article_teaser_body\").text\n",
    " \n",
    "print(f\"The title is: \\n{news_title}\")\n",
    "print()\n",
    "print(f\"The descriptive paragraph is:  \\n{news_paragraph}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "# find the featured image for Mars\n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA22911_ip.jpg'"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scrape the image from website\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')\n",
    "images = soup.find('a',class_='fancybox')\n",
    "images.attrs['data-fancybox-href']\n",
    "featured_image_url = 'https://www.jpl.nasa.gov'+images.attrs['data-fancybox-href']\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Weather \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open url in browser\n",
    "weather_url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(mars_weather_url)\n",
    "\n",
    "# create a soup item\n",
    "html_weather = browser.html\n",
    "soup = BeautifulSoup(html_weather, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "#Scrape the twitter data\n",
    "mars_weather = soup.find_all('div', class_='js-tweet-text-container')\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Value\n",
       "Description                                        \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Mars facts url \n",
    "facts_url = 'http://space-facts.com/mars/'\n",
    "\n",
    "# Use Panda's `read_html` to parse the url\n",
    "mars_facts = pd.read_html(facts_url)\n",
    "\n",
    "# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`\n",
    "mars_df = mars_facts[0]\n",
    "\n",
    "# Assign the columns `['Description', 'Value']`\n",
    "mars_df.columns = ['Description','Value']\n",
    "\n",
    "# Set the index to the `Description` column without row indexing\n",
    "mars_df.set_index('Description', inplace=True)\n",
    "\n",
    "# Save html code to folder Assets\n",
    "mars_df.to_html()\n",
    "\n",
    "data = mars_df.to_dict(orient='records')  # Here's our added param..\n",
    "\n",
    "# Display mars_df\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open url in browser\n",
    "hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(hemispheres_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# HTML Object\n",
    "html_hemispheres = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html_hemispheres, 'html.parser')\n",
    "\n",
    "# Retreive all items that contain mars hemispheres information\n",
    "items = soup.find_all('div', class_='item')\n",
    "\n",
    "# Create empty list for hemisphere urls \n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# Store the main_ul \n",
    "hemispheres_main_url = 'https://astrogeology.usgs.gov'\n",
    "\n",
    "# Loop through the items previously stored\n",
    "for i in items: \n",
    "    # Store title\n",
    "    title = i.find('h3').text\n",
    "    \n",
    "    # Store link that leads to full image website\n",
    "    partial_img_url = i.find('a', class_='itemLink product-item')['href']\n",
    "    \n",
    "    # Visit the link that contains the full image website \n",
    "    browser.visit(hemispheres_main_url + partial_img_url)\n",
    "    \n",
    "    # HTML Object of individual hemisphere information website \n",
    "    partial_img_html = browser.html\n",
    "    \n",
    "    # Parse HTML with Beautiful Soup for every individual hemisphere information website \n",
    "    soup = BeautifulSoup( partial_img_html, 'html.parser')\n",
    "    \n",
    "    # Retrieve full image source \n",
    "    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']\n",
    "    \n",
    "    # Append the retreived information into a list of dictionaries \n",
    "    hemisphere_image_urls.append({\"title\" : title, \"img_url\" : img_url})\n",
    "    \n",
    "\n",
    "# Display hemisphere_image_urls\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2 - MongoDB and Flask Application\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.6 64-bit ('Emmanuel': virtualenv)",
   "language": "python",
   "name": "python37664bitemmanuelvirtualenv2ccb626d4d184f9e92a8b2f7b4e6511b"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
