/*
1 = greetings
2 = afk
3 = thankfull
4 = command
5 = lust
6 = hentai
*/

select * from emote_bot_patterns;

insert into
	emote_bot_patterns
values 
	(1, 1, 'greetings'),
	(2, 1, 'hi'),
	(3, 1, 'hello'),
	(4, 1, 'good morning'),
	(5, 1, 'good evening')

insert into
	emote_bot_patterns
values 
	(6, 3, 'ty'),
	(7, 3, 'thanks'),
	(8, 3, 'thank you')
    
	
SELECT distinct response.response from emote_bot_response response LEFT JOIN emote_bot_tag tag ON response.tag_id = tag.id LEFT JOIN emote_bot_patterns patterns ON patterns.tag_id = tag.id  where patterns.patterns = 'thank you' order by RAND() limit 1

select distinct patterns.patterns from emote_bot_patterns patterns 

insert into
	emote_bot_patterns
values 
	(9, 4, 'lust')
	
insert into
	emote_bot_patterns
values
	(10, 5, 'how are you?'),
    (11, 5, 'are you ok?'),
    (12, 5, 'are you in a good mood?')
    