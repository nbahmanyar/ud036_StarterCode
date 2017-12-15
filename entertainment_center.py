import media
import fresh_tomatoes


# BEGIN block of code to define movie instances
thin_blue_line = media.Movie("Thin Blue Line",
							 "Crime Documentary",
							 "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/The_Thin_Blue_Line_poster.jpg/220px-The_Thin_Blue_Line_poster.jpg",
							 "https://www.youtube.com/watch?v=oEb_2mj1V8w"
							)
fire_at_sea = media.Movie("Fire at Sea",
							 "Documentary about the Struggles of Italian Migrants",
							 "https://upload.wikimedia.org/wikipedia/en/e/ee/Fire_at_Sea.jpg",
							 "https://www.youtube.com/watch?v=mbTcre_Sbno"
							)
city_of_ghosts = media.Movie("City of Ghosts",
							 "Documentary about Activists in Syria",
							 "https://upload.wikimedia.org/wikipedia/en/7/7a/City_of_Ghosts_%282017_film%29.png",
							 "https://www.youtube.com/watch?v=jBeqGcMaC-A"
							)
# END block of code to define movie instances



# Generate and open the movie website
movie_list = [thin_blue_line, fire_at_sea, city_of_ghosts]
fresh_tomatoes.open_movies_page(movie_list)
