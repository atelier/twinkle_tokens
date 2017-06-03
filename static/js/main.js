var jsonLyrics = {
		"variations": [
		{
			"title": "Original",
			"lines": [
				{"time": "[00:00.000]", "phrase": "Twinkle, twinkle, little star"}, 
				{"time": "[00:08.307]", "phrase": "How I wonder what you are."}, 

				{"time": "[00:12.347]", "phrase": "Up above the world so high"}, 
				{"time": "[00:16.443]", "phrase": "Like a diamond in the sky."}, 

				{"time": "[00:20.531]", "phrase": "When the blazing sun is gone"}, 
				{"time": "[00:24.588]", "phrase": "When he nothing shines upon,"}, 

				{"time": "[00:28.659]", "phrase": "Then you show your little light"}, 
				{"time": "[00:32.707]", "phrase": "Twinkle, twinkle, all the night."}, 

				{"time": "[00:36.835]", "phrase": "Then the traveler in the dark"}, 
				{"time": "[00:40.811]", "phrase": "Thanks you for your tiny spark,"}, 

				{"time": "[00:44.915]", "phrase": "He could not see which way to go"}, 
				{"time": "[00:48.955]", "phrase": "If you did not twinkle so."}, 

				{"time": "[00:53.051]", "phrase": "In the dark blue sky you keep"}, 
				{"time": "[00:57.091]", "phrase": "And often through my curtains peep,"}, 

				{"time": "[01:01.155]", "phrase": "For you never shut your eye"}, 
				{"time": "[01:05.259]", "phrase": "Till the sun is in the sky."}, 
			]
		},
		{
			"title": "v1",
			"lines": [
				{"time": "[00:00.000]", "phrase": "After roaming many lands,"}, 
				{"time": "[00:08.307]", "phrase": "Silent glowing northern lights."}, 

				{"time": "[00:12.347]", "phrase": "I believe in you, my soul,"}, 
				{"time": "[00:16.443]", "phrase": "Not sea-waves hurry in and out."}, 

				{"time": "[00:20.531]", "phrase": "As the contest hinged on thee,"}, 
				{"time": "[00:24.588]", "phrase": "Touch my body back again."}, 

				{"time": "[00:28.659]", "phrase": "It is dark here under ground,"}, 
				{"time": "[00:32.707]", "phrase": "Friendly faces yound and old."}, 

				{"time": "[00:36.835]", "phrase": "From the myriad thence-arous'd words"}, 
				{"time": "[00:40.811]", "phrase": "Let them know your scarlet heat."}, 

				{"time": "[00:44.915]", "phrase": "My real self has yet to come forth,"}, 
				{"time": "[00:48.955]", "phrase": "As I heard you shouting loud."}, 

				{"time": "[00:53.051]", "phrase": "In the nick of time I come"}, 
				{"time": "[00:57.091]", "phrase": "The sparrow with its simple notes,"}, 

				{"time": "[01:01.155]", "phrase": "As he rises he spouts blood,"}, 
				{"time": "[01:05.259]", "phrase": "Great shells shrieking as they pass."}, 
			]
		}
	]
}

var newSong, time, phrase, lrcArr, lrcStr;
newSong = jsonLyrics.variations[1];
time = 0;
phrase = "";
lrcArr = [];
lrcStr = "";

// iterate over lines and push to lrcArr
for (var i = 0; i < newSong.lines.length; i++) {
	phrase = newSong.lines[i].phrase;
	time = newSong.lines[i].time;
	lrcArr.push(time + phrase);
};
// build the string and join w/ linebreaks
lrcStr = lrcArr.join('\n');

console.log(lrcStr);

// var lyrics = "[ti:Twinkle Twinkle Lyric Star]\n[offset:3000]\n[00:00.000] Twinkle, twinkle, little star,\n [00:08.307] How I wonder what you are.\n[00:12.347] Up above the world so high,\n [00:16.443] Like a diamond in the sky.\n[00:20.531] When the blazing sun is gone,\n [00:24.588] When he nothing shines upon,\n[00:28.659] Then you show your little light,\n [00:32.707] Twinkle, twinkle, all the night.\n[00:36.835] Then the traveler in the dark,\n [00:40.811] Thanks you for your tiny spark,\n[00:44.915] He could not see which way to go,\n [00:48.955] If you did not twinkle so.\n[00:53.051] In the dark blue sky you keep,\n [00:57.091] And often through my curtains peep,\n[01:01.155] For you never shut your eye,\n [01:05.259] Till the sun is in the sky."
// var lyrics = "[ti:Twinkle Twinkle Little Whitman]\n[offset:0]\n[00:00.000] After roaming many lands,\n [00:08.307] Silent glowing northern lights.\n[00:12.347] I believe in you, my soul,\n[00:16.443] Not sea-waves hurry in and out.\n[00:20.531] As the contest hinged on thee,\n[00:24.588] Touch my body back again.\n[00:28.659] It is dark here under ground,\n[00:32.707] Friendly faces yound and old.\n[00:36.835] From the myriad thence-arous'd words\n[00:40.811] Let them know your scarlet heat.\n[00:44.915] My real self has yet to come forth,\n[00:48.955] As I heard you shouting loud.\n[00:53.051] In the nick of time I come\n[00:57.091] The sparrow with its simple notes,\n[01:01.155] As he rises he spouts blood,\n[01:05.259] Great shells shrieking as they pass."
var lyrics = lrcStr;

var lrc = new Lyricer(
		{
			"showLines": 1, 
			"clickable": false
		}
	);
lrc.setLrc(lyrics);

var audio = document.getElementById('song');
audio.addEventListener( "timeupdate", function() {
	lrc.move(audio.currentTime);
});
