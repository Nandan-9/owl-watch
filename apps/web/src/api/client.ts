const BASE_URL = "http://127.0.0.1:8000";

export async function apiRequest(
  endpoint: string,
  options: RequestInit = {}
) {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data?.message || "API Error");
  }

  return data;
}