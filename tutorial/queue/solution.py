##########################################################################
# In this practice problem you will implement a priority queue to 
# represent a music playlist queue. 
#
# It must meet the following requirements:
# * It must take an array representing a playlist already existing. In 
#   this array each index holds a song and the queue will play each song
#   in the passed in array.
#
# * The user must be able to turn on and off the repeat playlist feature. 
#   If the feautre is turned on the playlist will repeat back to the first 
#   song when it reaches the end. Otherwise it will stop playing. 
#
# * The user must be able to select a song from the playlist and queue it 
#   to play next.
#
# * The user must be able to select a song not in the playlist and queue 
#   it to play next. 
##########################################################################

class Playlist_Queue:
    """
    A class to implement a music playlist queue.
    """

    class Song:
        """
        Defines a Song for the music playlist.
        """

        def __init__(self, name, priority):
            """
            Initialize the song
            """
            self.name = name
            self.priority = priority

        def __str__(self):
            """
            Return a string representing the record so we can print it out later
            """
            return self.name 

    def __init__(self, song_names=[]):
        """
        Here we will initialize a new music playlist queue. 
        It takes an optional array of song names
        This constructor will create a queue of Song objects from
        the passed in song names.
        """
        # If there are no songs passed in then we don't need to do anything
        if len(song_names) == 0:
            self.queue = [] 

        # Otherwise asssign the same priority to all songs
        else:
            self.queue = []
            for name in song_names:
                song = Playlist_Queue.Song(name, 1) 
                self.queue.append(song)
    
        self.repeat = False

    def queue_song(self, name):
        """
        Here we will define a function that allows 
        the user to queue a new song. It automatically has a higher
        priority because when you queue a song it should play next.
        """

        # Create the song object and add it to the queue
        song = Playlist_Queue.Song(name, 2)
        self.queue.append(song)

    def _play_next_song(self, playlist):
        """
        Here we will define a function to play the next song. It 
        takes a playlist as a parameter. The next song played will 
        be the song with the highest priority. If there are multiple 
        songs with the same priority, we will play them in order of 
        first added to the queue.
        """

        if len(playlist) == 0:  # Verify the queue is not empty
            print("The playlist is empty.")

        # Find the index of the item with the highest priority 
        high_pri_index = 0
        for index in range(1, len(playlist)):
            if playlist[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
            elif playlist[index].priority > playlist[high_pri_index].priority:
                if index < high_pri_index:
                    high_pri_index = index
        # Play the song with the highest priority
        song = playlist[high_pri_index]
        playlist.pop(high_pri_index)
        print(f"Playing: '{song.name}'")

    def play(self):
        """
        Here we will define a function that will dicatate the play the playlist.
        It will look at the repeat bool for the playlist.
        If set to true, it will call the play on repeat function. If not it will
        play normally.
        """
        repeat = input("Play on repeat? (y/n)")
        if repeat.lower() == "y":
            self.repeat = True

        if self.repeat == False:
            self._play_normal()
        else:
            self._play_repeat()
    
    def _play_normal(self):
        """
        A function to play the playlist normally (Not on repeat)
        """
        # make a copy to keep the original array intact
        current_queue = list(self.queue)
        for i in range(len(current_queue)):
            self._play_next_song(current_queue)
    
    def _play_repeat(self):
        """
        A function to play the playlist on repeat
        """
        while self.repeat:
            # make a copy to keep the original array intact
            current_queue = list(self.queue)
            for i in range(len(current_queue)):
                self._play_next_song(current_queue)
            cont = input("repeat? (y/n)")
            if cont.lower() == "n":
                self.repeat = False

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        playlist queue.  This is useful for debugging.  If you have a 
        playlist object called pl, then you run print(pl) to see the 
        contents.
        """
        result = "[size=" + str(len(self.queue)) + " => "
        for song in self.queue:
            # Uses the __str__ from Song class
            result += "{"+str(song)+"}"
            result += ", "
        result += "]"
        return result







##########################################################################
# TESTS
#
# Now we will run a few tests to make sure that this queue works as
# expected and to exercise it's power.
##########################################################################

# Test 1: Play a existing playlist
song_list = ["Thriller" , "Come and Get Your Love", "Hotel California"]
playlist = Playlist_Queue(song_list)
print(playlist)
playlist.play()

# Test 2: Queue Song and play
song_list = ["Thriller" , "Come and Get Your Love", "Hotel California"]
playlist = Playlist_Queue(song_list)
print(playlist)
playlist.queue_song('I feel fine')
playlist.play()