css = '''


<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #2b333e
}
.chat-message .avatar {
    width: 15%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 85%
    padding: 0 1.5rem;
    color: #fff;
}
.bot-message{
padding:0.8rem;
}

.user-message{
padding:0.4rem;
}
</style>
'''

bot_template = '''
<div class = "chat-message bot">
    <div class="avatar">
        <img src="https://static.javatpoint.com/htmlpages/images/robot.jpg">
    </div>
    <div class="bot-message message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class= "chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ_Ks_IHTTwSjER6yTjpi2tBVyUvq9lVlQGA&usqp=CAU">
    </div>
    <div class = "user-message message">{{MSG}}</div>
</div>
'''