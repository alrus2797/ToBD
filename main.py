from lab1.data import Data


music_data = Data(open('music.csv','r'))
print("Music data headers: ",music_data.headers)
music_data.distances('Hailey','Veronica').manhattan()
music_data.distances('Hailey','Jordyn').euclidean()
music_data.distances('Angelica', 'Bill').minkowski(1)
music_data.distances('Angelica', 'Bill').minkowski(2)
print()

movie_data = Data(open('Movie_Ratings.csv','r'))
print("Movie data headers: ", movie_data.headers)

movie_data.distances('Heather','Bryan').manhattan()
movie_data.distances('Heather','Bryan').euclidean()
movie_data.distances('Heather','Bryan').minkowski(1)
movie_data.distances('Heather','Bryan').minkowski(2)