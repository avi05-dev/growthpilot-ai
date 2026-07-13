import { apiClient } from './client';
import type { DailyBriefing, ActionTask, KpiMetric } from '../features/dashboard/types/dashboard';

export type DashboardResponse = {
  briefing: DailyBriefing;
  actionTasks: ActionTask[];
  kpis: KpiMetric[];
};

export const DashboardApi = {
  async getDashboard(): Promise<DashboardResponse> {
    const response = await apiClient.get<DashboardResponse>('/api/dashboard');
    return response.data;
  },
};
