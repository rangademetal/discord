
select * from emote_bot_response
/*

emote response bot

1 = salutation
2 = bored
3 = thankfull
4 = command
5 = lust
6 = henati 

*/
insert into
	emote_bot_response
values
	(1, 1, 'Ohayō gozaimasu'),
	(2, 1, 'Konnichiwa'),
	(3, 1, 'Konbanwa'),

insert into
	emote_bot_response
values    
    (15, 1, 'https://cdn.discordapp.com/attachments/761138834523291668/831228104948449280/hat.gif')
    
insert into
	emote_bot_response
values
	(4, 2, '@everyone no one want to talk with a little blue hair girl?'),
	(5, 2, '@everyone is so boring here!! :weary:.'),
	(6, 2, '@everyone I have cookies!! If you make me happy, I can share some with you:blush:. '),
    (7, 2, '@everyone who want attention from me? Feel free to enjoy to talk with me :heart_eyes_cat:. '),
    (8, 2, '@everyone, are you there? I can not sleep.')
    
select response from emote_bot_response where tag_id=2 ORDER BY RAND() limit 1

insert into 
	emote_bot_response
values
	(9, 3, ':kissing_heart:'),
	(10, 3, ':hugging:'),
	(11, 3, 'With pleasure:kissing_heart:.'),
    (12, 3, 'No problem:hugging:.'),
    (13, 3, 'That why I am here, Senpai:kissing_heart:.'),
    (14, 3, 'I am here to help:hugging:.')

insert into 
	emote_bot_response
values
	(16, 5, 'Read some VN, you want to join me?'),
    (17, 5, 'Learning new things, are you curios?'),
    (18, 5, 'Watching my favorites anime, you should come with me and watch together:blush:.'),
    (19, 5, 'Clearing my room for party.'),
    (20, 5, 'Just brushing my hair for tonight:innocent:.'),
    (21, 5, 'Listen my new playlist from YouTube, can I share it with you :blush:?'),
    (22, 5, 'I am good.')
    
    
update emote_bot_response set response='Learning new things, are you curios?' where id=17
update emote_bot_response set response='Just brushing my hair for tonight:innocent:.' where id=20

insert into
	emote_bot_response
values
	(23, 6, 'Its my favourite one, please enjoy it:star_struck:.'),
    (24, 6, 'Cumming...:drooling_face:.'),
    (25, 6, 'Aww, thats one is all you need:blush:.'),
    (26, 6, 'Here we come:slight_smile:.'),
    (27, 6, 'Best manga ever.'),
    (28, 6, 'Tentacle? Check it:innocent:.'),
    (29, 6, 'Hmm, so good.'),
    (30, 6, 'Find one for you:smiling_face_with_3_hearts:.')
    