<template>
    <div class="comment-box">
        <p class="username">{{ username }}</p>
        <p class="comment">{{ commentValue }}</p>
        <p class="created_at">{{ created_at }}</p>
    </div>
</template>

<style scoped>
    .comment-box {
        margin: 0.4em;
        display: block;
        max-width: 90%;
        border-radius: 0.5em;
        box-shadow: 0 0.1em 0.1em 0.1em #dddddd;
        padding: 0.5em;
    }
    .comment-box>.username {
        font-weight: 600;
        text-align: left;
        margin: 0.2em 0 0.2em 0;
    }
    .comment-box>.comment {
        margin: 0;
        text-align: left;
    }
    .comment-box>.created_at {
        color: #bdbdbd;
        text-align: right;
        font-size: 8pt;
        margin: 0;
    }
</style>

<script>
    export default {
        name: 'Comment',
        props: {
            username: '유저 이름',
            commentValue: '댓글 내용',
            created_at: '생성 시각',
        }
    }
</script>