import { apiClient } from './client';

export type WorkspaceGenerateRequest = {
  domain: string;
  goal: string;
  time_window: string;
};

export type WorkspaceSource = {
  title: string;
  url: string;
  provider: string;
};

export type WorkspaceGenerateResponse = {
  summary: string;
  top_findings: string[];
  recommended_actions: string[];
  sources: WorkspaceSource[];
  generated_at: string;
  expires_at: string;
  cache_hit: boolean;
};

export const WorkspaceApi = {
  async generate(request: WorkspaceGenerateRequest): Promise<WorkspaceGenerateResponse> {
    const response = await apiClient.post<WorkspaceGenerateResponse>('/api/workspace/generate', request);
    return response.data;
  },
};
