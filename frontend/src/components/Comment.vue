<template>
    <div class="comment-box">
        <div class="header">
            <p class="username">{{ username }}</p>
            <p class="delete">삭제하기</p>
        </div>
        <p class="comment">{{ commentValue }}</p>
        <p class="created_at">{{ created_at }}</p>
    </div>
</template>

<style scoped>
    .comment-box {
        margin: 0.5em;
        display: block;
        max-width: 90%;
        border-radius: 0.5em;
        box-shadow: 0 0.1em 0.1em 0.1em #dddddd;
        padding: 0.5em;
    }
    .header {
        display: flex;
        width: 100%;
    }
    .header>.username {
        font-weight: 600;
        margin: 0.2em auto 0.2em 0;
    }
    .header>.delete {
        font-size: 9pt;
        color: #aaaaaa;
        margin: 0.2em 0 0.2em auto;
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