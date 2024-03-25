-- 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일 조회
-- 2022년 10월 작성
SELECT
    board.title, 
    board.board_id, 
    reply.reply_id, 
    reply.writer_id, 
    reply.contents, 
    TO_CHAR(reply.created_date, 'YYYY-MM-DD') AS created_date
FROM used_goods_board board, used_goods_reply reply
WHERE board.board_id = reply.board_id
AND EXTRACT(YEAR FROM board.created_date) = 2022
AND EXTRACT(MONTH FROM board.created_date) = 10
ORDER BY reply.created_date ASC, board.title ASC;