
# class Track:
# 	id: number;
# 	name: string;
# 	album_name: string;
# 	number: number;
# 	duration?: number;
# 	artists?: string[];
# 	youtube_id?: string;
# 	spotify_popularity: number;
# 	album_id: number;
# 	temp_id?: string;
# 	url?: string;
# 	users?: User[];
# 	lyric?: Lyric;
# 	plays: number = 0;
# 	album?: Album;
# 	playlists?: Playlist[];
# 		'id': fields.Integer,
#     'username': fields.String,
#     'email': fields.String,
#     'user_priority': fields.Integer,
#     'custom_greeting': fields.FormattedString('Hey there {username}!'),
#     'date_created': fields.DateTime,
#     'date_updated': fields.DateTime,
#     'links': fields.Nested({
#         'friends': fields.Url('user_friends', absolute=True),
#         'posts': fields.Url('user_friends', absolute=True),
#     }),
# class Album:
# id: number;
# 	name: string;
# 	release_date?: string;
# 	image?: string;
# 	artist_id?: number;
# 	spotify_popularity?: boolean;
# 	fully_scraped: boolean;
# 	temp_id?: string;
# 	artist?: Artist;
# 	tracks?: Track[];
#     views: number = 0;
#     auto_update: boolean = true;
