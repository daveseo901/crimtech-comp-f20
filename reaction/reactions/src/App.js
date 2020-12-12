import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    var obj = this;
    return function () {
        obj.setState({color: c});
    };
  }
  start_count() {
    this.setState({start_time: window.performance.now(), true_duration: getRandom(2, 7), counting: true, color: 'red'},
    function() { setTimeout(this.handle_color('green'), 1000 * this.state.true_duration); });
  }
  end_count() {
    let time = window.performance.now() - this.state.start_time;
    if (time > 1000 * this.state.true_duration) {
      this.setState({ran_once: true, counting: false, reaction_time: time - 1000 * this.state.true_duration});
    }
  }
  process_click() {
    console.log("clicked");
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "Hello World!";
      if (this.state.counting) {
        if (this.state.color === 'red') {
          msg = "Wait for Green";
        } else {
          msg = "Click!";
        }
      } else if (this.state.ran_once) {
        msg = "Your reaction time is " + String(this.state.reaction_time.toFixed(3)) + " ms";
      } else {
        msg = "Click me to begin!";
      }
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
