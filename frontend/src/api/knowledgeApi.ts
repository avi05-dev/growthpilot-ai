import { apiClient } from './client';

export type KnowledgeItem = {
  id: string;
  domain: string;
  title: string;
  summary: string;
  source: string;
  category: string;
  url: string | null;
  published_at: string | null;
  status: string;
  created_at: string;
  updated_at: string;
};

export type KnowledgeResponse = {
  knowledge: KnowledgeItem[];
};

export const KnowledgeApi = {
  async getKnowledge(): Promise<KnowledgeResponse> {
    const response = await apiClient.get<KnowledgeResponse>('/api/knowledge');
    return response.data;
  },
};
