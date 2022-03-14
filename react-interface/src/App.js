import { React, useState } from 'react';
import Widget from 'rasa-webchat';
import './App.css';

function App() {
  const [cleared, setCleared] = useState(false);

  const resetConversation = () => {
    console.log('reseting local storage');
    localStorage.clear();
    setCleared(true);
  };

  return (
    <div className="App">
      <div>
        <button onClick={resetConversation}>Restart</button>
      </div>
      <Widget
        socketUrl={"http://localhost:5005"}
        socketPath={"/socket.io/"}
        title={"Robot Grandkid"}
        // embedded={true}
        showFullScreenButton={true}
        subtitle={'Ask me about your tech problems'}
        storage={'local'}
      />
    </div>
  );
}

export default App;
