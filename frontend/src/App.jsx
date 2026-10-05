import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [summary, setSummary] = useState(null);
  const [summaryLoading, setSummaryLoading] = useState(true);

  useEffect(() => {
  const fetchSummary = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/summary");

      if (!response.ok) {
        throw new Error("Failed to fetch financial summary");
      }

      const data = await response.json();
      setSummary(data);
    } catch (err) {
      console.error("Summary error:", err);
    } finally {
      setSummaryLoading(false);
    }
  };

  fetchSummary();
}, []);

  const askFinAgent = async () => {
  if (!question.trim()) return;

  setLoading(true);
  setAnswer("");
  setError("");

  try {
    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: question,
      }),
    });

    if (!response.ok) {
      throw new Error(`Server returned ${response.status}`);
    }

    const data = await response.json();

    if (!data.answer) {
      throw new Error("FinAgent returned an empty response");
    }

    setAnswer(data.answer);
  } catch (err) {
    console.error("FinAgent error:", err);

    if (err instanceof TypeError) {
      setError(
        "Unable to reach the FinAgent server. Please make sure the FastAPI backend is running."
      );
    } else {
      setError(
        `FinAgent could not complete the analysis. ${err.message}`
      );
    }
  } finally {
    setLoading(false);
  }
};

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      askFinAgent();
    }
  };

  return (
    <div className="app">
      <div className="container">

        <header className="header">
          <div className="logo">₹</div>

          <div>
            <h1>FinAgent</h1>
            <p>AI Financial Analysis Assistant</p>
          </div>

          <div className="status">
            <span></span>
            Ollama AI
          </div>
        </header>

        <main>
          <section className="hero">
            <h2>Analyze your financial data with AI</h2>

            <p>
              Ask questions about revenue, expenses, profit, profit margins,
              growth and financial performance.
            </p>
          </section>
          <section className="summary-section">
            <div className="summary-header">
              <h3>Financial Overview</h3>
              <span>January – June</span>
            </div>

            {summaryLoading ? (
              <div className="summary-loading">Loading financial summary...</div>
            ) : summary ? (
              <div className="summary-grid">
                <div className="summary-card">
                  <span className="summary-label">Highest Revenue</span>
                  <strong>₹{summary.highest_revenue_month.revenue.toLocaleString("en-IN")}</strong>
                  <small>{summary.highest_revenue_month.month}</small>
                </div>

                <div className="summary-card">
                  <span className="summary-label">Highest Profit</span>
                  <strong>₹{summary.highest_profit_month.profit.toLocaleString("en-IN")}</strong>
                  <small>{summary.highest_profit_month.month}</small>
                </div>

                <div className="summary-card">
                  <span className="summary-label">Best Profit Margin</span>
                  <strong>{summary.highest_profit_margin_month.profit_margin}%</strong>
                  <small>{summary.highest_profit_margin_month.month}</small>
                </div>

                <div className="summary-card">
                  <span className="summary-label">Average Monthly Profit</span>
                  <strong>₹{summary.average_monthly_profit.toLocaleString("en-IN")}</strong>
                  <small>Across 6 months</small>
                </div>
              </div>
            ) : (
              <div className="summary-loading">
                Unable to load financial summary.
              </div>
            )}
          </section>

          <section className="chart-section">
            <div className="chart-header">
              <div>
                <h3>Revenue vs Profit</h3>
                <p>Monthly financial performance</p>
              </div>
            </div>

            {summary?.monthly_analysis && (
              <div className="chart-card">
                <ResponsiveContainer width="100%" height={320}>
                  <BarChart
                    data={summary.monthly_analysis}
                    margin={{ top: 10, right: 20, left: 10, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="month" />
                    <YAxis
                      tickFormatter={(value) =>
                        `₹${(value / 100000).toFixed(1)}L`
                      }
                    />
                    <Tooltip
                      formatter={(value, name) => [
                        `₹${Number(value).toLocaleString("en-IN")}`,
                        name,
                      ]}
                    />
                    <Legend />
                    <Bar dataKey="revenue" name="Revenue" fill="#3b82f6" />
                    <Bar dataKey="profit" name="Profit" fill="#22c55e" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            )}
          </section>

          <section className="chat-card">

            <label>Ask FinAgent</label>

            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Example: Which month had the highest profit?"
              rows="4"
            />

            <button
              onClick={askFinAgent}
              disabled={loading || !question.trim()}
              className={loading ? "analyzing" : ""}
            >
              {loading ? (
                <span className="loading-button">
                  <span className="spinner"></span>
                  Analyzing...
                </span>
              ) : (
                "Analyze"
              )}
            </button>

            {error && (
              <div className="error">
                {error}
              </div>
            )}

            {answer && (
              <div className="answer">
                <div className="answer-title">
                  FinAgent Analysis
                </div>

                <div className="answer-content">
                  <ReactMarkdown>{answer}</ReactMarkdown>
                </div>
              </div>
            )}

          </section>

          <section className="examples">
            <h3>Try asking</h3>

            <div className="example-grid">

              <button
                onClick={() =>
                  setQuestion("Which month had the highest profit?")
                }
              >
                Highest profit?
              </button>

              <button
                onClick={() =>
                  setQuestion("What was March's profit margin?")
                }
              >
                March profit margin?
              </button>

              <button
                onClick={() =>
                  setQuestion("Compare January and March.")
                }
              >
                Compare January & March
              </button>

              <button
                onClick={() =>
                  setQuestion("Which month had the highest revenue?")
                }
              >
                Highest revenue?
              </button>

            </div>
          </section>
        </main>

        <footer>
          <p>
            FinAgent • Powered by Ollama + Qwen3 + Python
          </p>
        </footer>

      </div>
    </div>
  );
}

export default App;