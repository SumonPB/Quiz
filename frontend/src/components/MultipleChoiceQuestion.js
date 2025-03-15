import React from 'react';

const MultipleChoiceQuestion = ({ question }) => {
  return (
    <div>
      <h3>{question.text}</h3>
      <ul>
        {question.answers.map(answer => (
          <li key={answer.id}>
            <input type="radio" name={`question-${question.id}`} value={answer.id} />
            <label>{answer.text}</label>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MultipleChoiceQuestion;