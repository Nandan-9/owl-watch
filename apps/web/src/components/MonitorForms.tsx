import { useState } from "react";
import { createMonitor } from "../api/monitor";

export default function MonitorForm() {
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResponse("");

    try {
      const data = await createMonitor(url);
      setResponse(JSON.stringify(data, null, 2));
    } catch (err: any) {
      setResponse(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Create Monitor</h2>

      <input
        type="text"
        placeholder="Name (optional)"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br /><br />

      <input
        type="text"
        placeholder="URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>

      <pre>{response}</pre>
    </div>
  );
}