from streamlit_elements import mui
from .dashboard import Dashboard


class Card(Dashboard.Item):

    def __call__(self,
                 title="Card title",
                 subheader="Card subheader",
                 content="Item content",
                 media=None,
                 avatar={'letter': 'A', 'bgcolor': 'red'},
                 overflow="auto"):

        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": overflow}, elevation=1):  # overflow: hidden|scroll|auto, overflowY: scroll
            mui.CardHeader(
                title=title,
                subheader=subheader,
                avatar=mui.Avatar(avatar['letter'], sx={"bgcolor": avatar['bgcolor']}),
                #action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class,
            )
            if media:
                # {"component": "img", "height": 194, "image": "https://mui.com/static/images/cards/paella.jpg", "alt": "Paella dish"}
                mui.CardMedia(**media)

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(content)

            # add a like and share button
            # with mui.CardActions(disableSpacing=True):
            #     mui.IconButton(mui.icon.Favorite)
            #     mui.IconButton(mui.icon.Share)
