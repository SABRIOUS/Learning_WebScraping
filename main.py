from bs4 import BeautifulSoup

SIMPLE_HTML = """
{% load staticfiles %}
{% load static %}
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">

  <title>codelist</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">


</head>

<body>
    <h1>This is me</h1>
    <p class="who">this is me</p>
    <p class="why">Learning step by step</p>
    <ul>
      <li>Ahmed</li>
      <li>sabry</li>
      <li>Mohamed</li>
      <li>Hard Worker</li>
    </ul>

  <nav>
    <div class="container nav-wrapper">
      <a href="/" class="brand-logo">Codedaddies List</a>
      <ul id="nav-mobile" class="right">
        <li><a href="/">Home</a></li>
      </ul>
    </div>
  </nav>
  <div class="container">
  <h1 style="text-align: center">What do you want to search for on codedlist?</h1>
  <div class="row">

    <div class="col s4">
      <div class="center">
        <i class="large material-icons" style="color:#EE6E73">flash_on</i>
        <p>Fast craigslist web scraper</p>
        <p class="light center">Scrap away right here with a beautiful GUI </p>
      </div>
    </div>

    <div class="col s4">
      <div class="center">
        <i class="large material-icons" style="color:orange">camera</i>
        <p class='who'>Filter your searches</p>
        <p class="light center">We built in functionality to filter based on pricing</p>
      </div>
    </div>

    <div class="col s4">
      <div class="center">
        <i class="large material-icons" style="color:blue">chrome_reader_mode</i>
        <p>A much easier front-end to craigslist</p>
        <p class="light center">We built this with ❤️</p>
      </div>
    </div>
  </div>
  <form action="{% url 'new_search' %}" method="post">
      {% csrf_token %}
      <input type="text" name="search" placeholder="search">
      <button class="btn waves-effect waves-light" type="submit" name="action">Submit
     <i class="material-icons right">send</i>
     </button>
  </form>


  {% block content %}
  {% endblock content %}
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>"""

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

def find_title():
        h1_tag = simple_soup.find("h1")
        print(h1_tag.string)

# find_title()


def list_items():
    list_item = simple_soup.find_all('li')
    new_list = [i.string for i in list_item]
    return new_list


# print(list_items())
def find_pgraph():
    get_p = simple_soup.find_all('p',{'class':'who'})
    new_p = [p.string for p in get_p]
    return new_p

# print(find_pgraph())

def other_graph():
    alparagraph = simple_soup.find_all('p')
    without_class = [p.string for p in alparagraph if 'who' not in p.attrs.get('class',[]) and 'why' not in p.attrs.get('class',[])]

    return without_class[0]

print(other_graph())
