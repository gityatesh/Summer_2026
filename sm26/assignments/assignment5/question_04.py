playlist = [
"Song-A",
"Song-B",
"Song-C",
"Song-D",
"Song-E"
]
song_to_remove = "Song-C"

for char in playlist:
    if char==song_to_remove:
        playlist.remove(char)
        
# print(playlist)

#we can also enqueue in the queue 
from datastructures.queues import queue
newplaylist=queue()
for char in playlist:
    if char != song_to_remove:
        newplaylist.enqueue(char)
        
newplaylist.showqueue()