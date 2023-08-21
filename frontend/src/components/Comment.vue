<template>
    <div class="comment-box">
        <div class="header">
            <p class="username">{{ username }}</p>
            <p @click="deleteComment" class="delete">삭제하기</p>
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
    import axios from 'axios';
    export default {
        name: 'Comment',
        props: {
            place_id: 0,
            comment_id: 0,
            username: '유저 이름',
            commentValue: '댓글 내용',
            created_at: '생성 시각',
        },
        methods: {
            deleteComment() {
                if (confirm("정말로 댓글을 삭제하시겠습니까?")) {
                    axios.delete(process.env.VUE_APP_BACKEND_ADDRESS+'/place/comment/'+this.place_id+'/', {
                    headers: { Authorization: 'Token '+sessionStorage.getItem('userToken') },
                    data: { 'comment_id': this.comment_id }
                    })
                    .then(res => {
                        alert("삭제되었습니다.")
                        console.log(res)
                    })
                    .catch(e => {
                        if (e.message == "Request failed with status code 403") alert("본인의 댓글만 삭제할 수 있습니다!")
                        else if (e.message == "Request failed with status code 401") alert("로그인 후 삭제하세요!")
                        else alert("오류가 발생했습니다.")
                    })
                }
            }
        }
    }
</script>