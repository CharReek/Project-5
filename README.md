# Reworn
## UX
Reworn is a website that provides users with a eco friendly way to shop.The green colour scheme represnts nature this help solidify the eco friendly nature of the website.
Users can browse different parts of the website by selecting what products they want to view. They can then view all the items they have in the shoipping bag and make a payment through Stripe payment. 
Users can also log into their account and view previous orders and change the saved delivery details

## Purpose
The purpose of this website is to stop more and more clothing ending up in landfills as this is an huge issue in todays society.The website provies a space where shoppers can find Substinably sources clothing that dosent hurt the enviroment.Users then can then make a purchase.

## Wireframes
All wireframs can be found in the media folder under Wireframes. 

I wanted my website to be clean and to the point as personally i hate when a webstire is cluttered. It makes things hard to find and gives the users a poor experience. This is somethign i kept in my mind though out the duration of the website design. 

## Userstories
All my user storeies can be found in the project board - [https://github.com/CharReek/Project-5/projects](https://github.com/CharReek/Project-5/projects)

I used these as a basis for my project to ensure that the website was catering to both the user and the store owner. 

## Exsisting Features
* ### Nav Bar & Drop down menu 
I opted for a slightly thicker nav bar that includes a set of dropdown menus to help the user navigate the site. On smaller devices the nav bar collapses into a drop down section making it more accessible for moblie users. 
* ### Footer
I kept this small with links to social media platform. I kept this small due to having a thicker nav bar. 
* ### Header image 
I chose to go for a thinner hero image as to not overpower the home page. I kept the colours of the images with in the colour scheme.I went for a picture of trees to bring the users mind back to nature as the websites main focus is ecofriendly fashion.
* ### Benefits
This reassures the user that shopping sustanibly has major benefits. This could also help user that have not thought aboput being more sustainable a shock on to how much harm is being caused. This will also help users feel good about purchasing form the site knwoing all the things they could help. Thererfore this will bring in new Shopper and user. 
* ### New in
This section can help entise users to spend longer on the site by giving them a look into what is new in. 
* ### Tips
This section provies Users/ shopper tips on how they can become more substainable. This may give the shopper some ideas of what they can do to upcycle clothing they already own.
* ### Shop 
Users can search for products in various different ways. once on the product page they also have the ability to sort the products. This can help users fidn what they are looking for and can even sort by price. This also caters to those who are on a budget giving them the opportunity to see products with in their price range. 
* ### Shopping bag
This ios where the user can see what they have in their bag. This gives the user the opportunity to review all the items that want to purcahse and update or remove anything they no longer want or want more of.This will reduce the amount of incorrect size purchases as the customer will be able to review what they have ordered. This page also works out shipping costs and add its to the users total. If the user is under the free shipping amount they will get message at the bottom telling them how far off they are from the free shipping amount. This could result in them purchasing extra items so they get free shipping. 
* ### Signin/ sign out / register functionality
This feature allows the customer to create an account and view past orders. users that have an account can save delivery details during the checkout. Those who do not have an account can register. There are mutiple different point that show a promt to register. i.e at the checkout to save any delivery information. 

## Future Features
There are mutiple features i would look to add in the future in order to provie the best and most effective user experience.
1. I would like to impliment a feature where other users can upload and sell any items they have. This way customers can swap items between each other.
2. Users be able to have visible profiles so they can follow each other and get notification on if their favourite user adds a new product. 
3. An FAQ page. This would be a space for users to look for answers to any questions they may have.
4. I would like to add a subscription section where customer can subscribe and get clothing delivered to them on a monthly basis. 

## Search engine Optimization
I implemented SEO techniques by researching key words. I found that the top 5 words were:
1. Substainable 
2. Eco-frienly
3. Fashion
4. Dresses
5. Eco 
I made sure i incliuded these words in the correct contect across the site.

I also made sure all images have alt tags. 
The site has a sitemap and a tobots.txt file 

## web marketing
Due to a trend in substainable fashion i decided to create an instagram page for Reworn. This was due to instagram being where the target audience in. The younger generation are becoming more and more concerned with fast fashion. The use of being able to tag a stor will help get the word about the store out there. 


## Technologies Used 
### Languages used 
* Html
* Css
* JavaScript
* Python 
* jQuery
* Django

### Technologies used 
* Github 
* Heroku
* Postgres
* Stripe payment
* AWS Bucket storage

### Frameworks and programs used
* Bootstrap 
* Fontawesome 
* Django 

## Code Validation
## Tests

## Bugs & soultions
* Stripe payment not Processing.
One major bug i experienced during this project was during the implimentation of stripe payment.Ii found that my payments were being created but were not successful. I spent many hourse searching solutions and went to tutor support for help. in the end it turend out to be that the webhook was not pulling the correct results due to a spelling error in the code. This was a simple fix however reading the stripe documentation gave me a good insight into the different functionalities that can be inplimented with stripe and i learned alot about how to find fixes for bugs.
* Non users being able to chekc out
This bug did not allow non users to chekc out, however once i fixed the above issue it also fixed this bug. 
## Unfixed bugs 
* There are no current bugs that i am aware of at the time od deployment. 

## Deployment and Cloning 

1. Ensure all requirements are in the requirements foler by typing "pip3 freeze --local > requirements.txt" in the terminal 
2. once this has been done git add, commit and push any changes made. 
### Heroku 
3. Load up heroku.com and log in. If you do not already have an account you will need to create one. 
4. Click the new button in the top right corner(for new users the button will appear in the center of the screen). Then choose 'Create new app'
5. Pick a name for your app- note this has to be unique.
6. Select your region
7. Then click create app
8. Once the app has been created navigate to the Resources tab go to add ons and search for Heroku Postgres
9. Go to setting - this can be found on the menu at the very top of the page
10. navigate to config vars. 
11. Reveal config vars and add the following variable to the list 
* Secret_key - this can be generated on websits such as [https://miniwebtool.com/django-secret-key-generator/](https://miniwebtool.com/django-secret-key-generator/)
### Code
12. Go back to your code and creat a Procfile at the base level
13. Place the below code into your Procfile
`web: gunicorn PROJ_NAME.wsgi`
14. Naviagte to setting and add heroku to the ALLOWED_HOSTS
15. Git add, commit and push the changes made.
### Deployment - Heroku
16. Go back to the heroku app and go to deploy in the menu bar.
17. Then go to the deployment method and select Github
18. Click connect to githhub and fins your github repository. 
19. Then click connect and scoll down to automatic deploys section
20. Select enable automatic deploys. 
21. Click deploy branch. 
22. This will take a few minutes to deploy and then click view. 
### Forking the github repository
Forking the repository means you are able to make a copy of the original repository meanign you can view and make changes without it affecting the origional repository
1. Log into github and find the Github repository you ware wanting to clone 
2. At the top of the repository (above settings) there will be a fork button. Click this
3. You will now have a copy of the reposiroty in your github account.
### Making a clone 
1. Log into git hub and go to the repository you want to clone
2. Under the name thewre will be a 'clone or download button. Click this 
3. Select clone by HTTPS and copy the link
4. open the commandline interface
5. Change the current working directory to the locationt that you want to cloned directory to be. 
6.  Type in `git clone` followed by the link you copied earlier and press enter 
Your local clone has been created

### Get stripe keys 
To access the stripe keys you will need to login and complete the following step
1. Once logged in go to the developers tab
2. One the left hand side there will be a tab for API keys select this. 
3. here youy will find the stripe public and secret key
Webhooks 
1. Go to the webhooks tab 
2. Select add end point
3. paste in your endpoint URL (this will be either your local or deployed url)
4. Select all event then click add endpoint
5. This will then redirect you to the webhooks page where you will be able to see the webhooks sign in secret 

### Getting email variables 
1. Log into Gmail acocunt 
2. Navigate to setting and then select all settings 
3. Then go to accoutns and import
4. go to Other google acocutn settings
5. Then Security 
6. Turn on 2 step verification 
7. Then go back to security app passwords
8. Select mail 
9. select device (other, django, Copy app password)
10. in heroku email_host_pass refers to the password copied fromt he above steps
11. Email_host_user is the gmail email account

### Setting AWS bucket up 
1. Go to Amazon web services page and either login in or create an account
2. If you are not redirected to the AWS management console you cna get to this by clicking on services icon and choosing Console home 
3. Click into All services and find S3 under storage 
4. Creat a new bucket using the button in the top right 
* Chose a name for your bucket and the region closest to you 
* enable ACLS 
* Ublock pubmlic access setting
5. Once you have clicked creat bucket you will be redirected to Amazon a3, this will have a listpof your buckets
6. Click into the one you have just created 
7. Navigate to the permissions tab on the top of the page and then go to Static web hosing. click edit slick enable and then fill in the index document.
8. on the permissions tab go to Cross origin resource sharing and paste in the below code 
`
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
`
9. Then go to bucket policy with in the permissions tab and edit the bucket policy. Select the following type of policy: S3 Bucket policy Principal: * (allows all) Actions: Get object Amazon Resource Name (ARN): then paste from the Edit bucket policy page in permissions 
10. Click Add statement
11. Then Click Generate Policy and Copy the policy into bucket policy editor.
12. Once you have done this got to the policy code and find Resource key and add "/*" after the name of the bucket to enable all Save changes
13. Then go to the Access control list in the permssion tab and click edit
14. Find Everyone(public access)check this box and then save 
15. Go back to the AWS management console and navigate to IAM in the services 
16. Go to user groups and selece creat group and name the group "manage-app-name" and click create 
17. go to policies and click create policy. Import managed policy and paste in the Amazons3FullAccess copr ARN to resources. 
18. Add list that contains  "[ "arn::..", ""arn::../*]"
19. click add tags and then click next and add a policy name and description and click create policy 
20. Attach the policy you created:
* go to user groups 
* selected the group form the list 
* navigate to permission from the dropdown chose attach policies 
* attach the policy you created and click add Permissions 
21. Create User in the group 
* Go to users in the side menu and select add user 
* user name will be your-app-staticfiles-user
* check options access key programmatic access and click the next button 
* add user group and the user to the group created.
* click creat user 
* download .csvf file 
22. Connect Django to the AWS s3 bucket 
* install boto3 
* install django-storages
* freeze requirements.txt
* add the below to storage and installed apps 
`if 'USE_AWS' in os.environ:'
    '# Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }' 
   `# Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' `

23. Next go to heroku and set up the environment variables 
* Go into the csv file that you downloaded and copy eash of the varaibles into the heroku settings
24. Create a file in the root directory called custom_storage.py 
` from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION `
25. Go inot settings.py and add the following AWS settings:
`# Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'`
`# Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/' `
26. Next you will need to load the media files to the s3 bucket 
27. Go to the bucket page 
28. Create new folder called media 
29. Go into the media folder and hit upload.

## Credits 
#### Images 
* I got my product images & my hero image from [https://unsplash.com](https://unsplash.com) all the individual artits can be found in the name of the image
#### Code 
* I used the Code Institue Boutique Ado walk though project as a guide through out various part of my project.
* Bootstrap Documentation to guide me with the collapsable navbar 
#### Online Resources
* [TinyPng](https://tinypng.com/) to make all my images an easier size for the website to handle 
* [https://www.befunky.com](https://www.befunky.com) photo editor to resize my images
* I got all my information about sustainability from [https://www.panaprium.com/blogs/i/eco-clothing](https://www.panaprium.com/blogs/i/eco-clothing).
#### Other 
* I would like to thank all those i work with for the continued suppport and motivation and for always helping me believe in myself.
* And all those from tutor support who helped me figure out any issues i had