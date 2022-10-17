post_data = [
    {
        "userId":  "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId":  "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId":  "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId":  "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId":  "Alex Gates",
        "id": 5,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    },
    {
        "userId":  "Alex Gates",
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia ",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
    }, ]

# Your Code Start from here
#catch the tile of each dictionary
for data in post_data:
    title=data.get("title")
   #remove the space from initial and last of the title
    if title[-1] or title[0] == " ":
        title = title[0:len(title) - 1]
        #replace the space of title with dash in slug
    slug_value = title.replace(" ", "-")
#date the dictionary
  #  data.update({'slug': slug_value})
  #  print(data)
    slug_split = slug_value.split("-")
    slug_length=len(slug_split)
    slug_split_value_3=(slug_split[0:3])
    final_slug_3="" #variable initialize
    #check the 1st 3 words of slug
    for x in slug_split_value_3:
        final_slug_3+=x+"-"
#remove the last slash (-)
    if final_slug_3[-1]=="-":
        final_slug_3=final_slug_3[0:len(final_slug_3)-1]
        # print slug limited to 3 words
        data.update({'slug': final_slug_3})
        print(data)
# Your code ends here
#print post_data[4]
print('\n','print post_data(4):', post_data[4])
