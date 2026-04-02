import { apiRequest } from "./client";

export async function createMonitor(url: string) {
  return apiRequest("/monitor/create/", {
    method: "POST",
    body: JSON.stringify({
      payload: url,
    }),
  });
}