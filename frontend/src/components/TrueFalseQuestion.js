import React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import Typography from '@mui/material/Typography';

const TrueFalseQuestion = ({ question }) => {
  return (
    <FormControl component="fieldset">
      <Typography variant="h6">{question.text}</Typography>
      <RadioGroup name={`question-${question.id}`}>
        {question.answers.map(answer => (
          <FormControlLabel
            key={answer.id}
            value={answer.id}
            control={<Radio />}
            label={answer.text}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
};

export default TrueFalseQuestion;