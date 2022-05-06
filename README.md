# BIRDWATCH_API

Access to pre-trained model and weights capable of classifying the ten UK garden birds.

- House Sparrow
- Blue Tit
- Starling
- Blackbird
- Woodpigeon
- Robin
- Great Tit
- Goldfinch
- Magpie
- Long-tailed Tit

Example CURL request:

curl --location --request POST 'http://127.0.0.1:5000/birdwatch' \
--form 'image=@[YOUR_FILE_PATH}'

![API Pipeline](https://user-images.githubusercontent.com/81023070/167101737-13dfcd31-a9ff-47b8-8e09-95339b44c372.png)
