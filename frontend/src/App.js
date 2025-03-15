import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MultipleChoiceQuestion from './components/MultipleChoiceQuestion';
import TrueFalseQuestion from './components/TrueFalseQuestion';

function App() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    axios.get('/api/questions/')
      .then(response => {
        setQuestions(response.data);
      })
      .catch(error => {
        console.error('Error fetching questions:', error);
      });
  }, []);

  return (
    <div>
      <h1>Preguntas</h1>
      {questions.map(question => (
        question.question_type === 'multiple_choice' ? (
          <MultipleChoiceQuestion key={question.id} question={question} />
        ) : question.question_type === 'true_false' ? (
          <TrueFalseQuestion key={question.id} question={question} />
        ) : (
          <div key={question.id}>
            <p>{question.text} (Tipo no soportado)</p>
          </div>
        )
      ))}
    </div>
  );
}

export default App;