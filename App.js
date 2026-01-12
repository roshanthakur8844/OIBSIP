import React, { useState } from 'react';
import BpkCalendar from 'bpk-component-calendar';
import BpkButton from 'bpk-component-button';
import { BpkText } from 'bpk-component-text';

import 'bpk-component-calendar/dist/bpk-calendar.css';
import 'bpk-component-button/dist/bpk-button.css';
import './App.scss';

function App() {
  const [selectedDate, setSelectedDate] = useState(null);

  const handleDateSelect = date => {
    setSelectedDate(date);
  };

  return (
    <div className="App">
      {/* Header */}
      <header className="App-header">
        <BpkText tagName="h1" textStyle="xl">
          Flight Schedule
        </BpkText>
      </header>

      {/* Calendar */}
      <div className="App-calendar">
        <BpkCalendar
          id="calendar"
          onDateSelect={handleDateSelect}
          selectedDate={selectedDate}
        />
      </div>

      {/* Button */}
      <div className="App-button">
        <BpkButton onClick={() => {}}>
          Continue
        </BpkButton>
      </div>
    </div>
  );
}

export default App;
