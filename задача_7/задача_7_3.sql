SELECT Books.title as book_title,
    Authors.first_name, Authors.last_name
FROM Books JOIN Authors ON Books.author_id = Authors.author_id