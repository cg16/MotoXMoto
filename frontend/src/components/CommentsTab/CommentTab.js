import React, { useState } from 'react';

const CommentsTab = () => {
  // Estado para armazenar a lista de comentários
  const [comments, setComments] = useState([]);
  // Estado para controlar o novo comentário que está sendo digitado
  const [newComment, setNewComment] = useState('');

  // Função para adicionar um novo comentário à lista de comentários
  const addComment = () => {
    if (newComment.trim() !== '') {
      setComments([...comments, newComment]);
      setNewComment('');
    }
  };

  return (
    <div>
      <h2>Comentários</h2>
      <ul>
        {comments.map((comment, index) => (
          <li key={index}>{comment}</li>
        ))}
      </ul>
      <div>
        <textarea
          value={newComment}
          onChange={(e) => setNewComment(e.target.value)}
          placeholder="Digite seu comentário..."
        />
        <button onClick={addComment}>Adicionar Comentário</button>
      </div>
    </div>
  );
};

export default CommentsTab;
