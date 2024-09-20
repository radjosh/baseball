import React from "react";

function App() {
  const ENDPOINT = "http://127.0.0.1:8899/player_war/";
  // const ENDPOINT = "http://localhost:8899";
  const [result, setResult] = React.useState([]);
  const [player, setPlayer] = React.useState('');

  async function handleSubmit(event) {
    event.preventDefault();
    const url = new URL(ENDPOINT);
    // url.searchParams.append("player", player.toLowerCase());
    const response = await fetch(url, {
      method: "GET",
    });
    // console.log(url);
    // console.log(player);
    const json = await response.json();
    setResult(() => JSON.parse(json));
    // setResult(() => json);
    console.log(json);
    setPlayer(() => "");
  }

  return (
    <div className="search">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          autoFocus
          value={player}
          onChange={(event) => {
            setPlayer(() => event.target.value);
          }}
        />
      </form>
      {/* {<SearchResults result={result} />} */}
      <ul>
          {result?.map(
            ([a, b]) => 
              <li key={crypto.randomUUID()}> Year: {a}, WAR: {b}</li>
          )}
      </ul>
    </div>
  );
}

export default App;
