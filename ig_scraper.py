from igramscraper.instagram import Instagram


def start_ig(username,password):
    instagram = Instagram()
    instagram.with_credentials(username,password,'./igcache')
    instagram.login()
    return instagram


def get_random_ig_images(username,password,tag,number_images = 5):
    instagram = start_ig(username,password)
    medias = instagram.get_medias_by_tag(tag,count = number_images)
    
    links = []
    for media in medias:
        links.append(media.image_high_resolution_url)

    return links
